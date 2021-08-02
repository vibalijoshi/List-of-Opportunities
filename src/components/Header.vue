<script setup lang="ts">
import { isDark, toggleDark } from '~/logic'
</script>

<template>
  <nav class="text-2xl my-6 flex flex-auto px-8 md:px-24">
    <router-link class="mx-2 text-gray-500 hover:text-blue-400" to="/" :title="'Home'">
      <mdi-handshake />
    </router-link>
    <div class="flex-grow">
      <!-- empty div because I am bad at CSS -->
    </div>
    <div class="">
      <button class="mx-2 !outline-none" :title="'Toggle Dark'" @click="toggleDark()">
        <carbon-moon v-if="!isDark" />
        <carbon-sun v-else class="text-yellow-300" />
      </button>

      <a
        class="mx-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-light-600"
        rel="noreferrer"
        href="https://github.com/vibalijoshi/List-of-Opportunities"
        target="_blank"
        title="GitHub"
      >
        <carbon-logo-github />
      </a>
    </div>
  </nav>
</template>
