import os
import shutil
from pathlib import Path
import logging

# the directory in which files are sorted
start_dir = "/home/pc/download"
# the directory to which sorted files are moved
gen_dir = "/home/pc/"

logging.basicConfig(level = logging.INFO, filename = "file_move_log.log", format = "%(asctime)s %(levelname)s %(message)s")

file_list = os.listdir(path=start_dir)
extensions_set = {
    "executable": [".sh", ".bash", ".zsh", ".py", ".pyc", ".pyo", ".pyw", ".pl", ".pm", ".t", ".rb", ".php", ".js", ".node", ".run", ".bin", ".AppImage", ".rpm", ".snap", ".flatpak", ".jar", ".war", ".ear", ".exe", ".msi", ".out", ".com", ".bat", ".cmd", ".ps1", ".scr", ".pif", ".reg"],
    "images": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".bmp", ".dib", ".tiff", ".tif", ".webp", ".ico", ".cur", ".svg", ".svgz", ".ai", ".eps", ".psd", ".raw", ".cr2", ".nef", ".arw", ".dng", ".xcf", ".ppm", ".pgm", ".pbm", ".pnm", ".heic", ".heif", ".emf", ".wmf"],
    "documents": [".pdf", ".txt", ".text", ".doc", ".docx", ".docm", ".dot", ".dotx", ".odt", ".fodt", ".rtf", ".pages", ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".ods", ".fods", ".csv", ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".odp", ".fodp", ".key", ".html", ".htm", ".xhtml", ".md", ".markdown", ".mdown", ".tex", ".latex", ".ltx", ".xml", ".xsl", ".xslt", ".epub", ".mobi", ".azw", ".azw3", ".fb2", ".fb2.zip", ".djvu", ".djv", ".chm", ".oxps", ".xps", ".one", ".pub", ".mpp", ".vsd", ".vsdx", ".accdb", ".mdb"],
    "audio": [".mp3", ".ogg", ".oga", ".opus", ".aac", ".m4a", ".mp4a", ".wma", ".wav", ".wave", ".flac", ".alac", ".aiff", ".aif", ".aifc", ".mid", ".midi", ".rmi", ".amr", ".ac3", ".au", ".snd", ".ra", ".rm", ".voc", ".8svx", ".cda", ".wax", ".m3u"],
    "video": [".mp4", ".m4v", ".mp4v", ".mpg4", ".avi", ".mkv", ".mov", ".qt", ".wmv", ".asf", ".flv", ".f4v", ".webm", ".mpeg", ".mpg", ".mpe", ".m1v", ".m2v", ".ts", ".mts", ".m2ts", ".tsv", ".tsa", ".vob", ".evo", ".3gp", ".3g2", ".ogv", ".rmvb", ".divx", ".dat", ".avi", ".mxf", ".swf", ".avchd", ".dvr-ms", ".wtv"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".gzip", ".bz2", ".xz", ".arc", ".arj", ".cab", ".cpio", ".deb", ".dmg", ".iso", ".lha", ".lzh", ".pkg", ".rpm", ".sit", ".sitx", ".z", ".zipx", ".pak", ".pk3", ".pk4", ".wad", ".bsa", ".apk", ".ipa", ".jar", ".xap"
    ],
    "other": []
}

for types, extension in extensions_set.items():
    if not os.path.isdir(gen_dir+types):
        os.mkdir(gen_dir+types)
    for filename in file_list:
        ex_file = os.path.splitext(filename)[-1]
        if ex_file in extension:
            shutil.move(start_dir + "/" + filename, gen_dir+types)
            logging.info(f"Файл {start_dir + "/" + filename} был перемещен в {gen_dir+types}")
        else:
             logging.warning(f"Файл {start_dir + "/" + filename} не был отсортирован ")



