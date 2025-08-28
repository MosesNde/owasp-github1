 
     @staticmethod
     def make_extract_command(inpath: str, outdir: str) -> List[str]:
        return ["tar", "xvf", inpath, "--directory", outdir]