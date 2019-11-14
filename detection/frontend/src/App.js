import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
} from 'react-router-dom';
import './App.css';
import { SettingsView, HomeView } from './views';

const App = () => (
  <div className="App">
    <header className="App-header">
      <h1>Open Spot</h1>
      <h2>Parking Solutions</h2>
    </header>
    <Router>
      <Switch>
        <Route path="/settings">
          <SettingsView />
        </Route>
        <Route path="/">
          <HomeView />
        </Route>
      </Switch>
    </Router>

  </div>
);

export default App;
