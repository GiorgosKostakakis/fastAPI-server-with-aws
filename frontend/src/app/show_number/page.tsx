async function ShowNumber() {
  const res = await fetch("http://127.0.0.1:8000/show_number");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function Page() {
  const data = await ShowNumber();

  return <main>
    <h1>Display Data</h1>
    <pre>{JSON.stringify(data, null, 2)}</pre>
  </main>;
}
