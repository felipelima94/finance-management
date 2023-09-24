import { GetServerSideProps, NextPage } from 'next'
import { Stock, Stocks } from '../models/stock'

const Home: NextPage<{stocks: Stock[] }> = ( {stocks} ) => {
  if( stocks == undefined ) {
    return
  }
  return (
    <>
      <h1>Wallet</h1>
      Total: {calcTotal(stocks)}
      <div className="stocks_tables">
        <div className="cell cell-head cell-1 code">Code</div>
        <div className="cell cell-head cell-1 total_purchased">Total Purchased</div>
        <div className="cell cell-head cell-1 total_sold">Total Sold</div>
        <div className="cell cell-head cell-1 total_invested">Total Invested</div>
        <div className="cell cell-head cell-1 amount">Amount</div>
        <div className="cell cell-head cell-1 avg_price">AVG Price</div>
        {stocks.map( (stock) => {
          return (<>
              <div className="cell cell-1 code">{stock.code}</div>
              <div className="cell cell-1 total_purchased">{stock.total_purchased}</div>
              <div className="cell cell-1 total_sold">{stock.total_sold}</div>
              <div className="cell cell-1 total_invested">{stock.total_invested}</div>
              <div className="cell cell-1 amount">{stock.amount}</div>
              <div className="cell cell-1 avg_price">{stock.avg_price}</div>
            </>
          )
        } )}
      </div>
    </>
  )
}

export const getServerSideProps: GetServerSideProps = async (context) => {
  // export const getStaticProps: GetStaticProps = async (context) => {
    let total = 0
    let stocks: Stocks = null
  try {
    const res = await fetch('http://localhost:8000/stock/prices')
    stocks = await res.json()
    
  } catch (error) {
    console.error(error)
  } finally {
    return { 
      props: {
        stocks: stocks,
        total: total
      }
    }
  }
}

export const calcTotal = (stocks: Stock[]) => {
  let total = 0
  stocks.forEach(stock => {
    total += stock.total_invested
  })
  return total
}

export default Home
