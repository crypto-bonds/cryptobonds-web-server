



action = payload.action
publicKey = txn.header.signerPublicKey

if(action == "Issuing_Bond_to_Bank") {
    return issuingBond(Bank,Company,numBonds)
}
elif(action == "Trader_Buys_Bank_Bond") {
    return buyBandBond(Bank,Company,numBonds,Trader)
}
elif(action == "Trader_Initiates_Trade") {
    return initiateTrade(BondA,BondANum,BondB,BondBNum)
}
elif(action == "Trader_Cancels_Trade") {
    return cancelTrade()
}
elif(action == "Trader_Accepts_Order") {
    return acceptOrder()
}
elif(action == "Add_Bitcoin") {
    return bitcoin()
}
else {
      throw new InvalidTransaction('Unknown action: ' + action);
}