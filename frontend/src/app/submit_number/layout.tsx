export default function SubmitNumberLayout () {
    return (
        <main>
            <h1>Submit a number</h1>
            <form>
                <label>
                    Number:
                    <input type="number" name="number" className="bg-gray-200 text-black" />
                </label>
                <button type="submit">Submit</button>
            </form>
        </main>
    );
}