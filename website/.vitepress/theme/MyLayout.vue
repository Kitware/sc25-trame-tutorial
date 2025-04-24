<!--.vitepress/theme/MyLayout.vue-->
<script setup>
import DefaultTheme from 'vitepress/theme'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #home-hero-image>
        <img src="/sc25-schedule.png" class="hero-pict"/>
    </template>
  </Layout>
</template>

<style scoped>
  .hero-pict {
    margin: 0;
  }
  @media (min-width: 960px) {
    .hero-pict {
        max-height: 385px;
        margin-left: 50px;
    }
  }
</style>