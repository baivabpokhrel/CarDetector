import React, { useState } from 'react';
import styles from './Image.module.css'
const Image = ({ srcBefore, srcAfter, ...props }) => {
  const [visibleImage, setVisibleImage] = useState(true)

  return (
    <div className={styles.image} {...props}>
      <img src={visibleImage ? srcBefore : srcAfter} {...props} onClick={() => setVisibleImage(!visibleImage)} alt={visibleImage ? "Parking Lot image" : "Parking lot image with overlay"} />
    </div>
  )
}

export default Image;
