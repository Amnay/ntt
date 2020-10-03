
class Monitor;

    mailbox#(Transaction) mon2ckr;
    
    function new(input mailbox#(Transaction) mon2ckr);
        this.mon2ckr = mon2ckr;
    endfunction
    
    virtual task run();
        Transaction tr;
        
        forever begin
            @ifc.cb;
            tr.left     <= ifc.cb.left;
            tr.rght     <= ifc.cb.rght;
            tr.modulo   <= ifc.cb.modulo;
            mon2ckr.put(tr);
        end
    endtask

endclass
