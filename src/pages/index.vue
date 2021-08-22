<script setup lang="ts">
import { useHead } from '@vueuse/head'
import { opportunities } from '~/logic/opportunities'

useHead({
  title: 'List of Opportunities',
  meta: [
    {
      name: 'description',
      content: 'Never miss a deadline again!',
    },
  ],
})

const search = ref('')

const matchFilter = (pattern: string, loc: string) => {
  const search = pattern.toLowerCase()
  const searchSpace = loc.toLowerCase()
  return searchSpace.includes(search)
}

const filteredOps = computed(() => {
  const searchVal = search.value.trim()
  return opportunities.filter(el => matchFilter(searchVal, el.name) || matchFilter(searchVal, el.type) || matchFilter(searchVal, el.deadline))
})
</script>

<template>
  <div class="px-4 md:px-32">
    <h1 class="text-2xl md:text-4xl text-center custom-text-bold">
      List of Opportunities
    </h1>
    <div class="text-center py-10">
      <input
        id="searchbar"
        v-model="search"
        type="text"
        name="search"
        autocomplete="off"
        placeholder="Name, month or type"
        class="py-10 searchbar"
      />
    </div>
    <div class="visible md:hidden text-center text-sm tracking-wide pb-5">
      Scroll sideways for more details <carbon-arrow-right class="pt-2" />
    </div>
    <div
      class="shadow sm:rounded-lg"
    >
      <table class="opptable table-auto">
        <thead>
          <tr>
            <th>Name</th>
            <th>Deadline</th>
            <th>Tags</th>
          </tr>
        </thead>
        <tbody v-if="filteredOps.length > 0">
          <tr v-for="opp in filteredOps" :key="opp.name + opp.deadline">
            <td>
              <a :href="opp.link" target="_blank" rel="noreferrer">
                {{ opp.name }}
                <bx-bx-link />
              </a>
            </td>
            <td>{{ opp.deadline }}</td>
            <td>{{ opp.type }}</td>
          </tr>
        </tbody>
        <div v-else class="text-xl text-center p-10">
          No results
        </div>
      </table>
    </div>
  </div>
</template>

<style scoped lang="postcss">
.searchbar {
  @apply rounded-full w-full border-1 focus:outline-none focus:ring focus:border-blue-300 py-4 px-6 leading-tight focus:outline-none dark:bg-dark-800;
}
tr>th, td>a{
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
}
</style>

<route lang="yaml">
meta:
  layout: default
</route>
