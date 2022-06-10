import React from "react";
import ReactDOM from "react-dom/client";
import Films from "./App";
import PostCountry from "./PostCountry";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <Films>Make your Query</Films>
    <PostCountry></PostCountry>
  </>
);
