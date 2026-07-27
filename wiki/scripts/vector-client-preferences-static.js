(function () {
  "use strict";

  const root = document.documentElement;
  const storagePrefix = "human-infra-vector-clientpref-";
  const preferences = {
    "vector-feature-custom-font-size": {
      options: [ "0", "1", "2" ],
      fallback: "1"
    },
    "vector-feature-limited-width": {
      options: [ "1", "0" ],
      fallback: "1"
    },
    "skin-theme": {
      options: [ "os", "day", "night" ],
      fallback: "day"
    }
  };

  function classValue(feature, options) {
    const prefix = `${feature}-clientpref-`;
    const match = Array.from(root.classList).find((name) => {
      return name.startsWith(prefix) && options.includes(name.slice(prefix.length));
    });
    return match ? match.slice(prefix.length) : null;
  }

  function storedValue(feature, options) {
    try {
      const value = localStorage.getItem(storagePrefix + feature);
      return options.includes(value) ? value : null;
    } catch (_error) {
      return null;
    }
  }

  function apply(feature, value, persist) {
    const { options } = preferences[feature];
    for (const option of options) {
      root.classList.remove(`${feature}-clientpref-${option}`);
    }
    root.classList.add(`${feature}-clientpref-${value}`);
    if (persist) {
      try {
        localStorage.setItem(storagePrefix + feature, value);
      } catch (_error) {
        // The preference still applies for this page when storage is unavailable.
      }
    }
    window.dispatchEvent(new Event("resize"));
  }

  for (const [feature, config] of Object.entries(preferences)) {
    const value = storedValue(feature, config.options)
      || classValue(feature, config.options)
      || config.fallback;
    apply(feature, value, false);
    const input = document.getElementById(
      `skin-client-pref-${feature}-value-${value}`
    );
    if (input) input.checked = true;
  }

  document.getElementById("vector-appearance")?.addEventListener(
    "change",
    (event) => {
      const input = event.target;
      if (!(input instanceof HTMLInputElement) || input.type !== "radio") return;
      for (const [feature, config] of Object.entries(preferences)) {
        if (input.name === `skin-client-pref-${feature}-group`
          && config.options.includes(input.value)) {
          apply(feature, input.value, true);
          return;
        }
      }
    }
  );
}());
