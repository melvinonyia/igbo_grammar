
////
//
// Root Component
//
////

import React from "react";
import { Provider } from "react-redux";
import { HashRouter } from "react-router-dom";
import App from "./app";

const Root = ({ store }) => (

  // Pass store to deeply nested components
  <Provider store={store}>
    <HashRouter>
      <App />
    </HashRouter>
  </Provider>
);

export default Root;
