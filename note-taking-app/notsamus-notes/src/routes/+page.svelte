<script lang="ts">
  import { onMount } from 'svelte';

  let newTask = '';
  let tasks: string[] = [];
  const STORAGE_KEY = 'notsamus-tasks';

  // Save tasks array to localStorage
  function saveTasks() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
      console.log('✅ Tasks saved to localStorage');
    } catch (e) {
      console.error('❌ Failed to save tasks:', e);
    }
  }

  // Load tasks array from localStorage
  function loadTasks() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        tasks = JSON.parse(raw);
        console.log('✅ Tasks loaded from localStorage:', tasks);
      }
    } catch (e) {
      console.error('❌ Failed to load tasks:', e);
      tasks = [];
    }
  }

  function addTask() {
    const t = newTask.trim();
    if (!t) return;
    tasks = [...tasks, t];
    newTask = '';
    saveTasks();
  }

  function removeTask(i: number) {
    tasks = tasks.filter((_, idx) => idx !== i);
    saveTasks();
  }

  onMount(() => {
    loadTasks();
  });
</script>

<h1>NotSamus To-Do List 📝</h1>

<input
  class="input-tasks"
  bind:value={newTask}
  placeholder="Add a new task"
/>
<button on:click={addTask}>Add</button>

<ul>
  {#each tasks as task, i}
    <li on:click={() => removeTask(i)}>
      {task}
    </li>
  {/each}
</ul>

<style>
  :global(body) {
    font-family: sans-serif;
    padding: 20px;
    max-width: 400px;
    margin: auto;
  }
  ul { list-style: none; padding: 0; }
  li { margin-bottom: 8px; cursor: pointer; }
  .input-tasks {
    width: 70%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
</style>
