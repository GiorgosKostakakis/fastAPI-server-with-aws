async function DisplayData() {
  const res = await fetch("http://127.0.0.1:8000/display_data");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function Page() {
  const data = await DisplayData();

  return <main>
    <h1>Display Data</h1>
    <pre>{JSON.stringify(data, null, 2)}</pre>
  </main>;
}
