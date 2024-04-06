export default function Home() {
  return (
    <main>
      <h1>Home</h1>
      <div className="flex flex-row space-x-4">
        <a
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          href="/submit_number"
        >
          Submit Number
        </a>
        <a
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          href="/show_number"
        >
          Show Number
        </a>
        <a
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          href="/display_data"
        >
          Display Data
        </a>
      </div>
    </main>
  );
}
