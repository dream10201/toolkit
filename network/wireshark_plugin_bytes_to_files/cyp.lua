cyp_proto = Proto ("cyp","cyp","cyp Protocol")

function cyp_proto.dissector(tvb,pinfo,tree)
    pinfo.cols.protocol:set("cyp")
    local buffer_len = tvb:len()
    local byte_array = tvb():bytes(ENC_STR_HEX)
    
    file = io.open("O:/pro/cyp.out","a")
    file:write(tostring(byte_array))
    file:close()
    return
end

local tcp_port_table = DissectorTable.get("tcp.port")
local my_port = 443
tcp_port_table:add(my_port, cyp_proto)
