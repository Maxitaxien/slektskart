type TextEntryProps = {
  placeholder: string;
  value: string;
  onChange: (value: string) => void;
  type?: string;
};

export default function TextEntry({
  placeholder,
  value,
  onChange,
  type = "text",
}: TextEntryProps) {
  return (
    <div className="w-full max-w-sm min-w-[200px]">
      <input
        className="w-full bg-transparent placeholder:text-dark text-sm border border-lightgreen rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-darkgreen hover:border-lightergreen shadow-sm focus:shadow"
        placeholder={placeholder}
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}
