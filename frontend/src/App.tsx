import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <section id="center">
        <div>
          <h1>
            My Personal Project
          </h1>
        </div>
        <div>
          <h1>Password Vault</h1>
            <p>Username: <input></input></p>
            <p>Password:  <input ></input></p>
        </div>
        <button
          type="button"
          className="counter"
          onClick={() => setCount((count) => count + 1)}
        >
          Log In
        </button>
      </section>
    </>
  )
}

export default App
