async function SubmitNumber(number: string) {
  const res = await fetch(`http://127.0.0.1:8000/submit_number/${number}`);
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function SubmitPage() {
  return (
    <main>
      <h1>Display Data</h1>
    </main>
  );
}
