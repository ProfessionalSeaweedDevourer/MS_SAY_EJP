import { configureStore } from "@reduxjs/toolkit";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";
import loginSystemSummonSlice from "./slice/loginSystemSummonSlice.js";
import memberSlice from "./slice/memberSlice.js";
import snsPostUpdateFormSlice from "./slice/snsPostUpdateFormSlice.js";

const msAISAStore = configureStore({
   reducer: {
      lsss: loginSystemSummonSlice,
      ms: memberSlice,
      spufs: snsPostUpdateFormSlice,
   },
});

createRoot(document.getElementById("root")).render(
   <Provider store={msAISAStore}>
      <BrowserRouter>
         <App />
      </BrowserRouter>
   </Provider>
);
