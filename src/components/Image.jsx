export default function Image({ src, ...rest }) {
  src =
    src && src.includes("https://")
      ? src
      : "http://localhost:4000/uploads/" + src;
  return (
    <img
      {...rest}
      src={src}
      alt={""}
      className="w-full h-full object-cover max-w-96 rounded-2xl"
    />
  );
}
