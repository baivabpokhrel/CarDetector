import React, { useState, useEffect } from 'react';
import Axios from 'axios'

import { SpotCount, Image, SpotList } from '../../components';

// const baseUrl = 'http://127.0.0.1:8000';
const baseUrl = 'http://35.245.136.196:81'
const HomeView = () => {
  const [data, setData] = useState({});
  const request = async () => {
    const result = await Axios(
      `${baseUrl}/api`,
    );

    setData(result.data)
  }

  useEffect(() => {
    request()
    setInterval(async () => await request(), 30000)
  }, []);
  const { image, imageMasked, availableSpots, totalSpots, openSpotsList, takenSpotsList } = data;
  console.log(openSpotsList)
  // console.log(response)
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
      <Image srcBefore={baseUrl + image} srcAfter={baseUrl + imageMasked} style={{ width: '40vw', height: 'calc(40vw/1.92)' }} />

      <SpotCount availableSpots={availableSpots} totalSpots={totalSpots} />
      <SpotList openSpotsList={typeof openSpotsList == 'string' && JSON.parse(openSpotsList)} takenSpotsList={typeof takenSpotsList == 'string' && JSON.parse(takenSpotsList)} />
    </div>
  );
};

export default HomeView;
