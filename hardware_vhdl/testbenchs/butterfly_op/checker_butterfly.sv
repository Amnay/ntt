
class Checker;

    mailbox#(Transaction) mdl2ckr;
    mailbox#(Transaction) mon2ckr;
    
    function new(input mailbox#(Transaction) mdl2ckr, input mailbox#(Transaction) mon2ckr);
        this.mdl2ckr = mdl2ckr;
        this.mon2ckr = mon2ckr;
    endfunction
    
    virtual task run();
        Transaction tr;
        
        forever begin
            @ifc.cb;
            mdl2ckr.get(tr_mdl);
            mon2ckr.get(tr_mon);
            
        end
    endtask

endclass
