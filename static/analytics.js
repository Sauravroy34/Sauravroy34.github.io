(function (document, posthog) {
  if (posthog.__SV) return;

  window.posthog = posthog;
  posthog._i = [];
  posthog.init = function (token, config, name) {
    function bind(target, method) {
      var parts = method.split(".");
      if (parts.length === 2) {
        target = target[parts[0]];
        method = parts[1];
      }
      target[method] = function () {
        target.push([method].concat(Array.prototype.slice.call(arguments)));
      };
    }

    var script = document.createElement("script");
    script.type = "text/javascript";
    script.crossOrigin = "anonymous";
    script.async = true;
    script.src = config.api_host.replace(".i.posthog.com", "-assets.i.posthog.com") + "/static/array.js";

    var firstScript = document.getElementsByTagName("script")[0];
    firstScript.parentNode.insertBefore(script, firstScript);

    var instance = posthog;
    if (name !== undefined) {
      instance = posthog[name] = [];
    } else {
      name = "posthog";
    }

    instance.people = instance.people || [];
    instance.toString = function (includeName) {
      var base = "posthog";
      if (name !== "posthog") base += "." + name;
      return includeName ? base : base + " (stub)";
    };
    instance.people.toString = function () {
      return instance.toString(1) + ".people (stub)";
    };

    [
      "init", "capture", "register", "register_once", "unregister", "opt_out_capturing",
      "has_opted_out_capturing", "opt_in_capturing", "reset", "isFeatureEnabled",
      "onFeatureFlags", "getFeatureFlag", "getFeatureFlagPayload", "reloadFeatureFlags",
      "updateEarlyAccessFeatureEnrollment", "getEarlyAccessFeatures", "identify",
      "setPersonProperties", "group", "resetGroups", "setPersonPropertiesForFlags",
      "resetPersonPropertiesForFlags", "setGroupPropertiesForFlags", "resetGroupPropertiesForFlags",
      "get_distinct_id", "getGroups", "get_session_id", "get_session_replay_url",
      "alias", "set_config", "startSessionRecording", "stopSessionRecording"
    ].forEach(function (method) {
      bind(instance, method);
    });

    posthog._i.push([token, config, name]);
  };
  posthog.__SV = 1;
})(document, window.posthog || []);

(function () {
  var POSTHOG_KEY = "phc_kVdnWB458tdtxaZJuAb5wZhjQfPeGVfQ7HVBino8USYV";
  var POSTHOG_HOST = "https://us.i.posthog.com";

  function routeType(path) {
    if (path === "/") return "home";
    if (path === "/posts/" || path === "/posts") return "post_index";
    if (/^\/posts\/[^/]+\/?$/.test(path)) return "post";
    return "other";
  }

  function routeProperties() {
    return {
      route: window.location.pathname,
      page_type: routeType(window.location.pathname)
    };
  }

  function classifyLink(url) {
    if (url.origin === window.location.origin) {
      if (/^\/posts\/[^/]+\/?$/.test(url.pathname)) return "article";
      if (url.pathname === "/index.xml") return "rss";
      return "navigation";
    }

    if (/^(github\.com|www\.linkedin\.com|linkedin\.com|x\.com|twitter\.com)$/.test(url.hostname)) {
      return "social";
    }
    if (url.hostname === "drive.google.com") return "cv";
    return "external_reference";
  }

  function sourceSection(link) {
    if (link.closest("footer, aside[role='contentinfo']")) return "footer";

    var path = window.location.pathname;
    if (path === "/" || /^\/page\/\d+\/?$/.test(path)) return "homepage";
    if (path === "/research/" || path === "/research") return "research_hub";
    return "post";
  }

  window.posthog.init(POSTHOG_KEY, {
    api_host: POSTHOG_HOST,
    autocapture: false,
    capture_pageview: false,
    capture_pageleave: false,
    disable_session_recording: true,
    person_profiles: "identified_only",
    persistence: "localStorage+cookie",
    defaults: "2025-05-24",
    loaded: function (analytics) {
      analytics.capture("$pageview", routeProperties());
    }
  });

  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[href]");
    if (!link) return;

    var href = link.getAttribute("href");
    if (!href || href.charAt(0) === "#" || href.indexOf("javascript:") === 0) {
      return;
    }

    if (href.toLowerCase().indexOf("mailto:") === 0) {
      if (!link.hasAttribute("data-research-contact")) return;

      window.posthog.capture("content_link_clicked", {
        route: window.location.pathname,
        source_section: sourceSection(link),
        target_type: "research_contact"
      });
      return;
    }

    var url;
    try {
      url = new URL(link.href, window.location.href);
    } catch (_error) {
      return;
    }

    if (url.protocol !== "http:" && url.protocol !== "https:") return;

    var properties = {
      route: window.location.pathname,
      source_section: sourceSection(link),
      target_type: classifyLink(url)
    };

    if (url.origin === window.location.origin) {
      properties.target_route = url.pathname;
    } else {
      properties.target_host = url.hostname;
    }

    window.posthog.capture("content_link_clicked", properties);
  });
})();
