import { useState ,  useEffect  , useRef} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import  Navbar from "./components/Navbar.jsx";

function App() {

const [form, setForm] = useState("")
const [todos, setTodos] = useState([])
const btnRef = useRef()
const [show, setShow] = useState(true)
useEffect(() => {
let todosString = localStorage.getItem("todos")
if(todosString) {
 const todo= JSON.parse(localStorage.getItem("todos"))
  setTodos(todo)
}
}, [])
const save =()=>{
  localStorage.setItem("todos" , JSON.stringify(todos))
}

const handleChange =  (e) => {
  setForm(e.target.value)
}
const handleAdd = () => {
  if (form.trim() === "") return; // prevent empty tasks
  setTodos([...todos, { text: form, done: false }]);
  // append new task
  setForm("");
save()

};

const handleEdit =  (i , text ) => {

  const newTodos = todos.filter((_, idx) => idx !== i);
  setTodos(newTodos); 
  
  setForm(text)
  


save()



}
const handleDel = (i) => {
  const newTodos = todos.filter((_, idx) => idx !== i);
  setTodos(newTodos);
save()

};

const handleDone = (i) => {
  const newTodos = todos.map((todo, idx) =>
    idx === i ? { ...todo, done: !todo.done } : todo
  );
  setTodos(newTodos);
save()

};

const showCompleted =  (e) => {
  setShow(!show)
 
  if (show) {
    btnRef.current.textContent = "Show Completed"
  }
  else {
    btnRef.current.textContent = "Hide Completed"
  }
  

}





  return (
    <>  
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-violet-50 dark:from-zinc-950 dark:via-zinc-950 dark:to-indigo-950 p-6 flex flex-col items-center">
      
      {/* Header */}
      <div className="flex items-center gap-3 mb-8">
        <div className="h-14 w-14 rounded-2xl bg-gradient-to-br from-indigo-500 via-violet-500 to-fuchsia-500 grid place-items-center shadow-lg">
          <span className="text-white text-2xl">✓</span>
        </div>
        <div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-500 via-violet-500 to-fuchsia-500 text-transparent bg-clip-text">
            Todo App
          </h1>
          <p className="text-sm text-gray-500">Beautiful gradient task manager</p>
        </div>
      </div>

      {/* Input Section */}
      <div className="w-full max-w-4xl flex flex-col sm:flex-row gap-3 mb-6">
        <input
          type="text"
          value = {form}
          onChange= {handleChange}
          placeholder="Add a new task..."
          className="flex-1 rounded-xl border px-4 py-3 shadow focus:outline-none focus:ring-2 focus:ring-violet-400"
          
        />
        <div className="flex gap-3">
          <button
            className="flex-1 sm:flex-none rounded-xl px-6 py-3 bg-gradient-to-r from-indigo-500 via-violet-500 to-fuchsia-500 text-white shadow-lg"
           onClick= {handleAdd}
          >
            Add
          </button>
       {   <button
            className="flex-1 sm:flex-none rounded-xl px-6 py-3 bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 text-white shadow-lg"
             onClick={showCompleted}
             ref= {btnRef}
          >
          Hide Completed
          </button>}
        </div>
      </div>

      {/* Task List */}
      <div  className="w-full max-w-4xl space-y-4">
      {todos.map((item, index) => (
    ((show || !item.done) && <div key={index} className="p-5 rounded-2xl border bg-white/80 dark:bg-zinc-900/80 shadow-lg flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:scale-[1.01] transition-transform">
 <div className="w-[300px]">
   <p className={   `${item.done?"line-through":''}   text-sm text-gray-800 dark:text-gray-300`}>{item.text}</p>
 </div>
 <div className="flex gap-2 flex-wrap">
   <button className="px-4 py-1.5 rounded-full bg-gradient-to-r from-green-500 to-emerald-600 text-white text-sm shadow"   onClick={()=>handleDone(index)}>Done</button>
   <button className="px-4 py-1.5 rounded-full bg-gradient-to-r from-sky-500 to-indigo-500 text-white text-sm shadow" onClick={()=>handleEdit(index , item.text) }>Edit</button>
   <button className="px-4 py-1.5 rounded-full bg-gradient-to-r from-rose-500 to-red-500 text-white text-sm shadow" onClick={()=>handleDel(index)}>Delete</button>
 </div>
</div> )
))}

       
</div>
    
    </div>
    </>
  )
}

export default App
