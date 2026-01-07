// import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import './index.css'
import App from './App.jsx'
import { configureStore } from '@reduxjs/toolkit'
// import { textSizeSlice } from './textSizeSlice.jsx'
import textReducer from './textSlice.jsx'
import { Provider } from 'react-redux'

// slice는 store에 등록된 것만 불러올 수 있다.
const reduxStore = configureStore({
    reducer: {
        text: textReducer,
    }
})

createRoot(document.getElementById('root')).render(

    <Provider store={reduxStore}>
        <App />
    </Provider>

)
