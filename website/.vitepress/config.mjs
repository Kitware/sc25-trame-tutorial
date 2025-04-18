import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: "/sc25-trame-tutorial",
  title: "Trame tutorial",
  description: "Trame tutorial for SuperComputing 2025",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Python', link: '/python' },
      { text: 'Jupyter', link: '/jupyter' },
      { text: 'Use cases', link: '/usecases' },
    ],

    sidebar: {
      "/python/": [
        {
          text: 'Getting Started',
          items: [
            { text: 'Setup Python', link: '/python/' },
          ]
        },
        {
          text: 'Trame fundamentals',
          items: [
            { text: 'Introduction', link: '/python/01/' },
            { text: 'MVVM Pattern', link: '/python/01/mvvm' },
            { text: '🏋️‍♂️ Hands on', link: '/python/01/run' },
            { text: 'Fundamentals', link: '/python/01/fundamentals' },
            { text: '🏋️‍♂️ Hands on', link: '/python/01/run2' },
            { text: 'Cheat sheets', link: '/python/01/cheat-sheets' },
          ]
        },
        {
          text: 'Dynamic web interface',
          items: [
            { text: 'Introduction', link: '/python/02/' },
            { text: 'Text interpolation', link: '/python/02/text' },
            { text: 'Raw HTML', link: '/python/02/raw' },
            { text: 'Attribute binding', link: '/python/02/attributes' },
            { text: 'Directives', link: '/python/02/directives' },
            { text: 'Event handling', link: '/python/02/events' },
            { text: 'JavaScript expressions', link: '/python/02/js' },
            { text: '🏋️‍♂️ Hands on', link: '/python/02/run' },
          ]
        },
        {
          text: 'Vuetify for beautiful UI',
          items: [
            { text: 'Introduction', link: '/python/03/' },
            { text: '🏋️‍♂️ Playground', link: '/python/03/playground' },
            { text: '🏋️‍♂️ trame convertion', link: '/python/03/playground-to-trame' },
            { text: '🏋️‍♂️ Many cards', link: '/python/03/dynamic-cards' },
            { text: '🏋️‍♂️ Animated content', link: '/python/03/animation' },
          ]
        },
        {
          text: '3D Visualization',
          items: [
            { text: 'Introduction', link: '/python/04/' },
          ]
        },
        {
          text: '2D Charts',
          items: [
            { text: 'Introduction', link: '/python/05/' },
          ]
        },
        {
          text: 'Interactive data processing',
          items: [
            { text: 'Introduction', link: '/python/06/' },
          ]
        },
      ],

      "/jupyter/": [
        {
          text: 'Getting Started',
          items: [
            { text: 'Setup Jupyter', link: '/jupyter/' },
          ]
        },
        {
          text: 'Trame fundamentals',
          items: [
            { text: 'Introduction', link: '/jupyter/01/' },
            { text: 'MVVM Pattern', link: '/jupyter/01/mvvm' },
            { text: '🏋️‍♂️ Hands on', link: '/jupyter/01/run' },
            { text: 'Fundamentals', link: '/jupyter/01/fundamentals' },
            { text: '🏋️‍♂️ Hands on', link: '/jupyter/01/run2' },
            { text: 'Cheat sheets', link: '/jupyter/01/cheat-sheets' },
          ]
        },
        {
          text: 'Dynamic web interface',
          items: [
            { text: 'Introduction', link: '/jupyter/02/' },
            { text: 'Text interpolation', link: '/jupyter/02/text' },
            { text: 'Raw HTML', link: '/jupyter/02/raw' },
            { text: 'Attribute binding', link: '/jupyter/02/attributes' },
            { text: 'Directives', link: '/jupyter/02/directives' },
            { text: 'Event handling', link: '/jupyter/02/events' },
            { text: 'JavaScript expressions', link: '/jupyter/02/js' },
            { text: '🏋️‍♂️ Hands on', link: '/jupyter/02/run' },
          ]
        },
        {
          text: 'Vuetify for beautiful UI',
          items: [
            { text: 'Introduction', link: '/jupyter/03/' },
            { text: '🏋️‍♂️ Playground', link: '/jupyter/03/playground' },
            { text: '🏋️‍♂️ trame convertion', link: '/jupyter/03/playground-to-trame' },
            { text: '🏋️‍♂️ Many cards', link: '/jupyter/03/dynamic-cards' },
            { text: '🏋️‍♂️ Animated content', link: '/jupyter/03/animation' },
          ]
        },
        {
          text: '3D Visualization',
          items: [
            { text: 'Introduction', link: '/jupyter/04/' },
          ]
        },
        {
          text: '2D Charts',
          items: [
            { text: 'Introduction', link: '/jupyter/05/' },
          ]
        },
        {
          text: 'Interactive data processing',
          items: [
            { text: 'Introduction', link: '/jupyter/06/' },
          ]
        },
      ],
      "/usecases/": [
        { text: 'Introduction', link: '/usecases/' },
        { text: 'Peacock 2.0', link: '/usecases/peacock' },
        { text: 'Blast code', link: '/usecases/blast' },
        { text: 'ArrowFlow', link: '/usecases/arrowflow' },
        { text: 'EPIC', link: '/usecases/epic' },
        { text: 'DAIMSAL', link: '/usecases/daimsal' },
        { text: '(XAI + NR).TK', link: '/usecases/xaitk-nrtk' },
      ]
    },
  }
})
