interface Props {
    confidence: number;
}

export default function ConfidenceBar({
    confidence,
}: Props) {

    const percent = Math.round(confidence * 100);

    return (

        <div>


            <div className="mb-3 flex items-center justify-between">

                <span className="text-lg font-semibold">
                    Confidence
                </span>

                <span className="font-bold text-green-600">
                    {percent}%
                </span>

            </div>

            <div className="h-3 w-full overflow-hidden rounded-full bg-gray-200">

                <div
                    className="h-full rounded-full bg-green-500 transition-all duration-500"
                    style={{
                        width: `${percent}%`,
                    }}
                />

            </div>

        </div>

    );

}