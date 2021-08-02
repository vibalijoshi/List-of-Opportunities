<script setup lang="ts">

import { useRouter } from 'vue-router'
const router = useRouter()
</script>
<template>
  <main class="px-4 py-10 text-center text-gray-700 dark:text-gray-200">
    <div>
      <h1 class="custom-text-bold text-3xl">
        This page does not exist!
      </h1>
      <p class="text-4xl">
        <carbon-warning class="inline-block" />
      </p>
    </div>
    <div>
      <button
        class="px-5 py-3 rounded-md bg-green-400 dark:bg-green-600 m-3 text-sm mt-8"
        @click="router.back()"
      >
        Go Back
      </button>
    </div>
  </main>
</template>

<route lang="yaml">
meta:
  layout: 404
</route>
