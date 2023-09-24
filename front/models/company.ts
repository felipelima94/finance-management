export interface Companys {
    companys: Company[];
}

export interface Company {
    id?:            string;
    fantasy_name?:  string;
    administrator?: string;
    code:           string;
    cnpj?:          string;
}
