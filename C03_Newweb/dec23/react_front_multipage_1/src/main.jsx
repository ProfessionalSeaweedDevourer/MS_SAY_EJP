import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import {BrowserRouter} from "react-router-dom"

createRoot(document.getElementById('root')).render(
    <BrowserRouter>
      <App />
    </BrowserRouter> // 페이지 전환 구현
)
