import { combineReducers } from "redux";

import loans from "./loansReducer";
import installments from "./installmentsReducer";
import notifications from "./notificationsReducer";
import loanNotif from "./notificationsReducer";
import application from "./applyLoanReducer";
import successloan from "./applyLoanReducer";
import counter from "./applyLoanReducer";

export default combineReducers({
    loans,
    installments,
    notifications,
    loanNotif,
    application,
    successloan,
    counter,
});