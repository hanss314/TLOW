$i = "ip#{?a}"
system "gem install string_to_#$i"
system "gem install pry" #if necessary
require "string_to_#$i"
def convert str
    str.chomp.send :"to_#$i"
end
