const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    // define URI base de acesso
    baseUrl: 'https://www.amazon.com.br',
    viewportWidth: 1920,
    viewportHeight: 1080,

    setupNodeEvents(on, config) {
      // node event listeners
    },
  },
});
