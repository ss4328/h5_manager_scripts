# tests/test_cli.py
import pathlib, subprocess, sys

PACKAGE_ROOT = pathlib.Path(__file__).parents[1]

def run_cli(*args):
    return subprocess.check_output([sys.executable, "-m", "h5manager.cli", *args]).decode()

def test_convert_then_visualize(tmp_path):
    img_dir = PACKAGE_ROOT / "examples" / "images" / "hotdog"
    out = tmp_path / "tiny"
    run_cli("convert", str(img_dir), "--output", str(out), "--dim", "16")
    assert out.with_suffix(".h5").exists()

def test_merge(tmp_path):
    img_dir = PACKAGE_ROOT / "examples" / "images" / "hotdog"
    a = tmp_path / "a"
    b = tmp_path / "b"
    run_cli("convert", str(img_dir), "--output", str(a), "--dim", "8")
    run_cli("convert", str(img_dir), "--output", str(b), "--dim", "8")
    merged = tmp_path / "merged"
    run_cli("merge", "--inputs", f"{a}.h5,{b}.h5", "--output", str(merged))
    assert merged.with_suffix(".h5").exists()
