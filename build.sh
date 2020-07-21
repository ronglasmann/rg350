
# ensure the dist folder exists
mkdir -p ./_dist && \

# --------------------------------------------------------------------------
# ball package build
# --------------------------------------------------------------------------

# Remove the existing bouncing ball opk.
rm -f ./_dist/bouncing_ball.opk && \

# Compile the ball.py to ball.pyc
python -m compileall ./ball -d ./_dist && \

# Create the OPK. It is a squashfs archive so we just list all the files and
# the last name will be the archive name,
mksquashfs  \
  ./ball/default.gcw0.desktop \
  ./ball/ball.pyc \
  ./ball/icon.png \
  ./ball/ball.png \
  ./_dist/bouncing_ball.opk \
  -all-root -no-xattrs -noappend -no-exports
