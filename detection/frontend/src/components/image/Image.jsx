import React, { useState } from 'react';
import styles from './Image.module.css'
const Image = ({ srcBefore, srcAfter, ...props }) => {
  const [visibleImage, setVisibleImage] = useState(true)

  return (
    <div className={styles.image} {...props}>
      <img src={visibleImage ? srcBefore : srcAfter} {...props} onClick={() => setVisibleImage(!visibleImage)} />
    </div>
  )
}

export default Image;
