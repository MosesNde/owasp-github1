         folder = (
             folder.replace("http://", "")
             .replace("https://", "")
             .replace(":", "")
             .replace("/", "_")
             .replace("\\", "_")