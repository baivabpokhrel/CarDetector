import React, { useState, useEffect } from 'react';
import cookie from 'js-cookie';

const SettingsView = () => {
  const devMode = cookie.get('devMode');
  if (devMode === undefined) {
    cookie.set('devMode', false)
  }
  const [isDevMode, setIsDevMode] = useState(devMode == 'true')
  return (
    <div>
      Settings
      <h2>Toggle Dev Mode</h2>
      <input type="checkbox" value={isDevMode} onChange={e => setIsDevMode(e.target.value == 'true')} />
    </div>
  )
};

export default SettingsView;
