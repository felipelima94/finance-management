import { NextPage } from "next";
import { useState } from "react";

const AddCompanyPage: NextPage = () => {

    const [company, setCompany] = useState({
        fantasy_name: '',
        administrator: '',
        code: '',
        cnpj: '',
    })

    const handleInput = (e) => {
        const fieldName = e.target.name;
        const fieldValue = e.target.value;

        setCompany((prevState) => ({
            ...prevState,
            [fieldName]: fieldValue
        }));
    }

    const submitForm = (e) => {
        e.preventDefault()

        const formURL = e.target.action
        const data = new FormData()

        // POST the data to the URL of the form
        fetch(formURL, {
            method: "POST",
            body: JSON.stringify(company),
            headers: {
                'Content-Type': 'application/json',
            },
        }).then((response) => onSuccess, () => alert('oops'))

        const onSuccess = (response) => {
            let responseDate = response.json()
            clearForm()
        }

        const clearForm = () => {
            setCompany({ 
                fantasy_name: '',
                administrator: '',
                code: '',
                cnpj: ''
            })
        }
        
    }

    return (
        <>
        <h1>Add Company</h1>
        <form className="form-company" method="POST" action="http://localhost:8000/company/create" onSubmit={submitForm}>
            <div>
                <label>Fantasy Name:</label> 
                <input type="text" name="fantasy_name" onChange={handleInput} value={company.fantasy_name}></input>
            </div>
            <div>
                <label>Administrator:</label> 
                <input type="text" name="administrator" onChange={handleInput} value={company.administrator}></input>
            </div>
            <div>
                <label>Code:</label> 
                <input type="text" name="code" onChange={handleInput} value={company.code} required></input>
            </div>
            <div>
                <label>CNPJ:</label> 
                <input type="text" name="cnpj" onChange={handleInput} value={company.cnpj}></input>
            </div>
            <div>
                <label>
                    <button type="submit" name="save">Save</button>
                </label>
            </div>
        </form>
        </>
    )
}

export default AddCompanyPage
