import { GetServerSideProps, NextPage } from 'next'
import { Company, Companys } from '../../models/company'

const CompanyList: NextPage<{company: Company[] }> = ( {company} ) => {
  
  return (
    <>
      <h1>Companys</h1>
      <div className="company-list-table">
        <div className="cell cell-head cell-1">FantasyName</div>
        <div className="cell cell-head cell-1">Administrator</div>
        <div className="cell cell-head cell-1">Code</div>
        <div className="cell cell-head cell-1">Cnpj</div>
        <div className="cell cell-head cell-1">Options</div>
        {company.map( (company) => {
          return (<>
            <div className="cell cell-1">{company.fantasy_name}</div>
            <div className="cell cell-1">{company.administrator}</div>
            <div className="cell cell-1">{company.code}</div>
            <div className="cell cell-1">{company.cnpj}</div>
            <div className="cell cell-1">Option</div>
            </>
          )
        } )}
      </div>
    </>
  )
}

export const getServerSideProps: GetServerSideProps = async (context) => {
  // export const getStaticProps: GetStaticProps = async (context) => {
  let company: Company = null
  try {
    const res = await fetch('http://localhost:8000/company/list')
    company = await res.json()
    
    
  } catch (error) {
    console.error(error)
  } finally {
    return { 
      props: {
        company: company
      }
    }
  }
}

export default CompanyList
