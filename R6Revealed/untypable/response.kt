fun r6(input: String) { var st = java.util.Stack<Long>()
 if(!input.startsWith("This is TLOWScript")) { println("NotTLOWException"); return }      
 var statements = "[^A-Za-z0-9 ]".toRegex().replace(input.substring(18), "").split(' '); var i = 0
 while(i < statements.size) { 
  when (statements[i]) { 
        "add"-> st.push(st.pop() + st.pop()); "printNum"-> print(st.pop())
   "multiply"-> st.push(st.pop() * st.pop()); "printChr"-> print(st.pop().toChar())
   "subtract"-> st.push(st.pop() - st.pop());      "dup"-> st.push(st.peek())
     "divide"-> st.push(st.pop() / st.pop());     "goto"-> i = st.pop().toInt()
         else-> st.push(statements[i].toLong()) }; i++ } }
