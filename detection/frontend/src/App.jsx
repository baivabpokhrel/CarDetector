import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import { Header, Grommet, Text, Heading } from 'grommet'
import './App.css';
import { SettingsView, HomeView } from './views';

const theme = {
  global: {
    font: {
      family: 'Roboto',
      size: '14px',
      height: '20px',
      color: '#fffff'
    },

  },
};

const App = () => (
  <Grommet theme={theme} style={{ backgroundColor: '#222831' }}>
    <Header style={{ color: '#eeeeee', paddingLeft: '2em', paddingRight: '2em' }}>
      <Heading bold color="#d65a31">Open Spot</Heading>
      <Text bold>Parking Solutions</Text>
    </Header>
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

  </Grommet>
);

export default App;
