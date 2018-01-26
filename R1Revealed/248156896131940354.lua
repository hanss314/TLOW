os.execute("ls * > file_list.txt")    -- Why Sally wrote a Lua script
all_files = io.lines("file_list.txt") -- instead of Bash is beyond me

os.remove("file_list.txt")

for file in all_files do
    os.rename(file, file.gsub(file, "%.php", ".txt"))
end