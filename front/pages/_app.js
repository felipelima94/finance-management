import styles from '../styles/main.css'

import Layout from './components/Layout'

export default function MyApp({ Component, pageProps }) {
    return (<Layout><Component {...pageProps} /> </Layout>)
  }