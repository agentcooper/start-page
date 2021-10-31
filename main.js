async function fetchTodayTasks() {
  const res = await fetch("http://localhost:9001/today");
  const result = await res.json();
  return result.tasks;
}

async function main() {
  const todayTasks = await fetchTodayTasks();

  const habitTasks = todayTasks.filter((task) => {
    return (
      Array.isArray(task.tags) &&
      task.tags.find((tag) => tag.toLowerCase() === "habits")
    );
  });

  document.getElementById("habit-tasks").textContent = habitTasks.length;
}

main();
