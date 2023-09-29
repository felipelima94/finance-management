export interface Stocks {
    stocks: Stock[];
}

export interface Stock {
    code:            string;
    total_purchased: number;
    total_sold:      number;
    total_invested:  number;
    amount:          number;
    avg_price:       number;
}
