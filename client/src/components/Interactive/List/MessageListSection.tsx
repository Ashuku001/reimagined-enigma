import { XIcon } from "lucide-react";
import { useParams } from "next/navigation";
import { Header } from "@/components/Interactive/SubComponents";
import { Button } from "@/components/ui/button";
import { PlusIcon, Rotate3DIcon } from "lucide-react";
import { UseFormReturn } from "react-hook-form";
import { Input } from "@/components/ui/input";
import { useInteractiveListStore, SectionType, RowType } from "@/store/InteractiveListStore";
import toast from "react-hot-toast";
import { Separator } from "@/components/ui/separator";
import { FormControl, FormField, FormItem } from "@/components/ui/form"
import { ProductsSwitcherListMessage } from "@/components/ProductsSwitcherListMessage";
import secureLocalStorage from 'react-secure-storage';
import { useRecommendationModal } from "@/hooks/useRecommendationModal";
import { useEffect, useState } from "react";


type MessageListProps = {
    form: UseFormReturn<{
        [key: string]: "";
    }, any, {
        [key: string]: "";
    }>
}


export const MessageListSections = ({form}: MessageListProps) => {
    const params = useParams()
    const recommendationModal = useRecommendationModal()
    const [rowsCount, sections, setRowsCount,  addSection, deleteSection, addRow] = useInteractiveListStore((state) => [
        state.rowsCount,
        state.sections,
        state.setRowsCount,
        state.addSection,
        state.deleteSection,
        state.addRow,
    ]) 

    const onAddSection = () => {
        if(rowsCount >= 10){
            toast.error("You can only add a total of 10 rows from all sections to the list message.", {
                duration: 6000
            })
        } else {
            setRowsCount(+1)
            addSection({
                id: Math.floor(Math.random() * 100),
                title: "",
                rows: [{
                    id: Math.floor(Math.random() * 100),
                    title: '',
                    description: '',
                    product: null
                }],
            })
        }
    }

    const onRecommend = () => {
        const customerId = params.customerId as unknown as number
        const merchantId = secureLocalStorage.getItem('merchantId') as number
        recommendationModal.onOpen({customerId: [customerId], merchantId})
    }

    const onDeleteSection  = (secIndex: number, section: SectionType) => {
        form.resetField(`sectionTitle-${secIndex}`)
        
        const rowFields = Object.keys(form.formState.dirtyFields)
        const deletedFields = rowFields.filter((field) => field.includes(`section-${secIndex}`))
        deletedFields?.forEach((field) =>{ 
            form.resetField(field)
        })

        setRowsCount(-section.rows.length)
        deleteSection(section.id)
    }


    return (
        <div className="p-1 relative">
            <Header variant='required' title='Section' description='Add sections for the list of products. Total rows from all sections is limited to 10.\nYou can also generate recommendation by clicking the button recommend.' />
            <div className="flex items-center justify-between">
                <Button className="mt-1 sticky top-0" variant={'secondary'} onClick={() => {onAddSection()}} type="button">
                    <PlusIcon className="h-4 w-4"/>
                    Add a Section (max 10)
                </Button>
                <Button className="mt-1 sticky top-0 flex space-x-2 items-center" variant={'secondary'} onClick={() => {onRecommend()}} type="button">
                    <Rotate3DIcon className="h-4 w-4"/>
                    Recommend
                </Button>
            </div>
            <div className="mt-3">
                {sections?.map((section: SectionType, secIndex: number) => 
                <div key={secIndex}  className="w-full">
                    <ListSection
                        secIndex={secIndex} 
                        section={section} 
                        sectionsLength={sections?.length}
                        onDeleteSection={onDeleteSection} 
                        form={form}
                    />
                    <Separator className="my-4" />
                </div>
                )}
            </div>
        </div>
    )
};


// #######################################################################

type ListSectionProps = {
    form: UseFormReturn<{
        [key: string]: "";
    }, any, {
        [key: string]: "";
    }>
    section: SectionType
    secIndex: number;
    sectionsLength: number;
    onDeleteSection: (secIndex: number, section: SectionType) => void;
}



export const ListSection = ({secIndex, sectionsLength, section, onDeleteSection, form,}: ListSectionProps) => {
    const [title, setTitle] = useState("")
    const [rowsCount, sections, setRowsCount, addRow, deleteRow, updateSectionTitle] = useInteractiveListStore((state) => [
        state.rowsCount,
        state.sections,
        state.setRowsCount,
        state.addRow,
        state.deleteRow,
        state.updateSectionTitle
    ])

    const onAddRow = (sectionId: number) => {
        if(rowsCount >= 10){
            toast.error("You can only add a maximum of 10 rows in the message")
        } else {
            const newRow = {id: Math.floor(Math.random() * 100), title: "", description: "", product: null}
            setRowsCount(+1)
            addRow(sectionId, newRow)
        }
    }

    const onDeleteRow = (rowIndex: number, secIndex: number, sectionId: number, rowId: number) => {
        form.resetField(`title-section-${secIndex}-row-${rowIndex}`)
        form.resetField(`description-section-${secIndex}-row-${rowIndex}`)
        deleteRow(sectionId, rowId)
        setRowsCount(-1)
    }
    
    useEffect(() => {
        setTitle(sections[secIndex].title)
    }, [sections, updateSectionTitle, secIndex])

    return (
        <div className="border-2 p-1">
            <div className="text-slate-300 py-2 text-center font-semibold flex justify-between">
                <div>Section {secIndex + 1}  </div>
                {(secIndex !== 0 && secIndex === sectionsLength -1 ) &&
                    <Button variant={'ghost'} size={'icon'} onClick={() => onDeleteSection(secIndex, section)}>
                        <XIcon className="h-4 w-4"/>
                    </Button>
                }
            </div>
            <div>
                <FormField
                    control={form.control}
                    name={`sectionTitle-${secIndex}`}
                    render={({field}) => (
                        <FormItem>
                            <FormControl>
                                <Input
                                    value={field.value ?? title}
                                    placeholder={`Section ${secIndex + 1} title`}
                                    onChange={(e) => {
                                        field.onChange(e.target.value);
                                        updateSectionTitle(section.id, {title: e.target.value})
                                    }}
                                /> 
                            </FormControl>
                        </FormItem>
                    )}
                />
                <Button className="mt-2" variant={'secondary'} onClick={() => {onAddRow(section.id)}} type="button">
                    <PlusIcon className="h-4 w-4"/>
                    Add a row to section {secIndex + 1}
                </Button>
                <div className="mt-3">
                    {section.rows?.map((row, rowIndex) => 
                        <Row
                            key={rowIndex}  
                            row={row}
                            section={section}
                            rowIndex={rowIndex} 
                            secIndex={secIndex} 
                            rowsLength={section.rows?.length} 
                            onDeleteRow={onDeleteRow} 
                            form={form}
                    />)}
                </div>
            </div>
        </div>
    )
}


// ###################################################################

type RowProps = {
    form: UseFormReturn<{
        [key: string]: "";
    }, any, {
        [key: string]: "";
    }>
    row: RowType;
    section: SectionType;
    rowIndex: number;
    secIndex: number;
    rowsLength: number;
    onDeleteRow: (index: number, secIndex: number, sectionId: number, rowId: number) => void;
}


export const Row = ({ row, section, onDeleteRow, form, rowIndex, secIndex, rowsLength,}: RowProps) => {
    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")
    //@ts-ignore
    const [updateRowTitle, updateRowDescription, sections] = useInteractiveListStore((state) => [
        state.updateRowTitle,
        state.updateRowDescription,
        state.sections
    ])
    useEffect(() => {
        setTitle(sections[secIndex].rows[rowIndex].title)
        setDescription(sections[secIndex].rows[rowIndex].description)
    }, [sections, setTitle, setDescription, rowIndex, secIndex])

    return(
        <div className="flex space-x-3 mt-2">
            <div className="flex-1 flex space-x-3">
                <FormField
                    control={form.control}
                    name={`title-section-${secIndex}-row-${rowIndex}`}
                    render={({field}) => (
                        <FormItem 
                        className="w-[30%]">
                            <FormControl>
                                <Input
                                    value={field.value ?? title}
                                    placeholder={`Title...`}
                                    onChange={(e) => {
                                        field.onChange(e.target.value);
                                        updateRowTitle(section.id, row.id, {title: e.target.value})
                                    }}
                                    className="w-full"
                                /> 
                            </FormControl>
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name={`description-section-${secIndex}-row-${rowIndex}`}
                    render={({field}) => (
                        <FormItem 
                        className="w-[50%]">
                            <FormControl>
                                <Input
                                    value={field.value ?? description}
                                    placeholder={`Description...`}
                                    onChange={(e) => {
                                        field.onChange(e.target.value);
                                        updateRowDescription(section.id, row.id, {description: e.target.value})
                                    }}
                                    className="w-full"
                                /> 
                            </FormControl>
                        </FormItem>
                    )}
                />
                <ProductsSwitcherListMessage sectionId={section.id} row={row}/>
            </div>
            <div className="w-5 flex items-center justify-center">
                {(rowIndex !== 0 && rowIndex === rowsLength -1 ) 
                ?   <Button type='button' variant={'ghost'}  size={'sm'} className="m-0 p-0" onClick={() => onDeleteRow(rowIndex, secIndex,  section.id, row.id,)}>
                        <XIcon className="h-4 w-4"/>
                    </Button>
                :   <Button variant={'ghost'} size={'sm'} disabled  className="m-0 p-0">
                    </Button>
                }
            </div>
        
        </div>
    )
}
