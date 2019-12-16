import React, { useState, useEffect } from 'react';
import Axios from 'axios'

import { SpotCount, Image } from '../../components';

const baseUrl = 'http://127.0.0.1:8000';
const HomeView = () => {
  const [data, setData] = useState({});
  useEffect(() => {
    const request = async () => {
      const result = await Axios(
        `${baseUrl}/api`,
      );

      setData(result.data)
    }
    request()
  }, []);
  const { image, imageMasked, availableSpots, totalSpots } = data;
  // console.log(response)
  return (
    <div>
      <Image srcBefore={baseUrl + image} srcAfter={baseUrl + imageMasked} style={{ width: '40vw' }} />

      <SpotCount availableSpots={availableSpots} totalSpots={totalSpots} />
    </div>
  );
};

export default HomeView;
