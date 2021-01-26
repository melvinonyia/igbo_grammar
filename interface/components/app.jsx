
////
//
// App Component
//
////

import React from "react";
import {
  Route,
  Redirect,
  Switch,
  Link,
  HashRouter
} from 'react-router-dom';
import { AuthRoute, ProtectedRoute } from '../utilities/route_utilities';

const App = () => (
  <div>
    <header>
      <Link to="/" className="header-link">
        <h1>Igbo Grammar</h1>
      </Link>
      <GreetingContainer />
    </header>
    <Switch>
      //<AuthRoute exact path="/login" component={LogInFormContainer} />
      //<AuthRoute exact path="/signup" component={SignUpFormContainer} />
      <ProtectedRoute exact path="/" component={CourseList} />
    </Switch>
  </div>
);

export default App;
